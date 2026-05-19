# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T18:22:22.995587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.0278` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.0367` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2438` n `12`; crypto_alt avg `-0.1711` n `228`; crypto_major avg `-0.101` n `8`; equity avg `-0.1077` n `66`; fx avg `0.0112` n `6`; index avg `0.2179` n `23`; metal avg `-0.1998` n `18`; unknown avg `-0.0706` n `383`
- 1h: commodity avg `-0.069` n `12`; crypto_alt avg `-0.2236` n `228`; crypto_major avg `-0.395` n `8`; equity avg `-0.1594` n `66`; fx avg `0.0184` n `6`; index avg `0.1207` n `23`; metal avg `-0.4503` n `18`; unknown avg `1.2875` n `383`
- 4h: commodity avg `0.2339` n `12`; crypto_alt avg `0.2812` n `228`; crypto_major avg `0.3796` n `8`; equity avg `2.4074` n `66`; fx avg `-0.0141` n `6`; index avg `1.4163` n `23`; metal avg `0.042` n `18`; unknown avg `1.453` n `383`
- 24h: commodity avg `0.3193` n `12`; crypto_alt avg `1.4461` n `228`; crypto_major avg `1.2392` n `8`; equity avg `1.5938` n `66`; fx avg `0.0572` n `6`; index avg `0.5048` n `23`; metal avg `-1.8571` n `18`; unknown avg `1.6858` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
