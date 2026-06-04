# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T22:07:20.958247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.7182` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.6721` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.5324` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.512` n `228`; crypto_major avg `-0.3522` n `8`; equity avg `-0.1061` n `74`; fx avg `-0.001` n `6`; index avg `-0.2538` n `23`; metal avg `0.0177` n `18`; unknown avg `-0.4992` n `424`
- 1h: commodity avg `-0.1347` n `12`; crypto_alt avg `-2.3749` n `228`; crypto_major avg `-1.7253` n `8`; equity avg `-0.1929` n `74`; fx avg `-0.0109` n `6`; index avg `-0.0532` n `23`; metal avg `-0.0071` n `18`; unknown avg `-0.7138` n `424`
- 4h: commodity avg `0.2488` n `12`; crypto_alt avg `-2.1346` n `228`; crypto_major avg `-1.1047` n `8`; equity avg `-0.9695` n `74`; fx avg `-0.0158` n `6`; index avg `-0.3385` n `23`; metal avg `-0.1493` n `18`; unknown avg `-0.8033` n `424`
- 24h: commodity avg `-0.6407` n `12`; crypto_alt avg `-8.1663` n `228`; crypto_major avg `-5.6596` n `8`; equity avg `-0.5596` n `73`; fx avg `0.0694` n `6`; index avg `0.1766` n `23`; metal avg `0.9248` n `18`; unknown avg `-1.0869` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
