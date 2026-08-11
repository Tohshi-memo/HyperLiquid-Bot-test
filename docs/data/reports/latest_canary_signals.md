# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T07:37:31.583421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.0767` n `230`; crypto_major avg `0.1845` n `8`; equity avg `0.1114` n `113`; fx avg `-0.0118` n `6`; index avg `0.0258` n `25`; metal avg `0.0516` n `20`; unknown avg `-0.0035` n `785`
- 1h: commodity avg `0.0768` n `12`; crypto_alt avg `-0.2568` n `230`; crypto_major avg `-0.0481` n `8`; equity avg `0.0729` n `113`; fx avg `-0.023` n `6`; index avg `0.0058` n `25`; metal avg `0.0155` n `20`; unknown avg `0.0415` n `785`
- 4h: commodity avg `0.3077` n `12`; crypto_alt avg `-0.5116` n `230`; crypto_major avg `-0.3072` n `8`; equity avg `-0.174` n `113`; fx avg `0.0061` n `6`; index avg `-0.0451` n `25`; metal avg `-0.3212` n `20`; unknown avg `0.0652` n `753`
- 24h: commodity avg `1.2099` n `12`; crypto_alt avg `-1.3703` n `230`; crypto_major avg `-1.2299` n `8`; equity avg `-1.4281` n `113`; fx avg `0.0329` n `6`; index avg `-0.047` n `25`; metal avg `0.075` n `20`; unknown avg `0.1118` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
