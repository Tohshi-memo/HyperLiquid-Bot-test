# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T22:37:23.453849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.9371` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6649` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.288` n `228`; crypto_major avg `-0.3359` n `8`; equity avg `-0.0985` n `74`; fx avg `0.0027` n `6`; index avg `-0.0028` n `23`; metal avg `0.014` n `18`; unknown avg `-0.3023` n `424`
- 1h: commodity avg `-0.2309` n `12`; crypto_alt avg `-0.6122` n `228`; crypto_major avg `-0.3039` n `8`; equity avg `-0.3337` n `74`; fx avg `-0.0061` n `6`; index avg `-0.137` n `23`; metal avg `0.0507` n `18`; unknown avg `-0.6873` n `424`
- 4h: commodity avg `-0.0032` n `12`; crypto_alt avg `-2.9618` n `228`; crypto_major avg `-1.9797` n `8`; equity avg `-1.181` n `74`; fx avg `-0.0222` n `6`; index avg `-0.3148` n `23`; metal avg `-0.0426` n `18`; unknown avg `-0.8023` n `424`
- 24h: commodity avg `-0.5248` n `12`; crypto_alt avg `-7.5706` n `228`; crypto_major avg `-5.1541` n `8`; equity avg `-0.5646` n `73`; fx avg `0.0522` n `6`; index avg `0.1958` n `23`; metal avg `0.9542` n `18`; unknown avg `-1.1025` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
