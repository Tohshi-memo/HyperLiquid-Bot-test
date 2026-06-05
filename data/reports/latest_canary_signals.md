# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T05:52:22.896028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6032` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.4909` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4805` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.2982` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0546` n `12`; crypto_alt avg `-0.6358` n `228`; crypto_major avg `-0.7178` n `8`; equity avg `-0.2667` n `74`; fx avg `0.0158` n `6`; index avg `-0.0852` n `23`; metal avg `0.0216` n `18`; unknown avg `1.5608` n `424`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.5613` n `228`; crypto_major avg `-0.8315` n `8`; equity avg `-0.117` n `74`; fx avg `-0.0072` n `6`; index avg `-0.0645` n `23`; metal avg `-0.0632` n `18`; unknown avg `-0.4244` n `424`
- 4h: commodity avg `0.0715` n `12`; crypto_alt avg `-2.366` n `228`; crypto_major avg `-2.5317` n `8`; equity avg `-0.2335` n `74`; fx avg `-0.0518` n `6`; index avg `-0.0512` n `23`; metal avg `-0.0408` n `18`; unknown avg `-1.4111` n `424`
- 24h: commodity avg `-0.152` n `12`; crypto_alt avg `-5.1178` n `228`; crypto_major avg `-4.9891` n `8`; equity avg `-1.4598` n `73`; fx avg `0.1765` n `6`; index avg `-0.5192` n `23`; metal avg `-0.4458` n `18`; unknown avg `-1.9518` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
