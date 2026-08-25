# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T18:18:31.813682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.2795` n `231`; crypto_major avg `0.2301` n `8`; equity avg `0.0841` n `122`; fx avg `-0.0044` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0083` n `20`; unknown avg `0.0669` n `795`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.4757` n `231`; crypto_major avg `0.5655` n `8`; equity avg `-0.0167` n `122`; fx avg `-0.0033` n `6`; index avg `-0.0155` n `25`; metal avg `0.0045` n `20`; unknown avg `0.1164` n `795`
- 4h: commodity avg `0.0107` n `12`; crypto_alt avg `0.4449` n `231`; crypto_major avg `0.7037` n `8`; equity avg `0.4935` n `122`; fx avg `-0.021` n `6`; index avg `0.0137` n `25`; metal avg `0.2035` n `20`; unknown avg `0.0701` n `795`
- 24h: commodity avg `-0.6017` n `12`; crypto_alt avg `-0.4168` n `231`; crypto_major avg `0.928` n `8`; equity avg `1.2891` n `122`; fx avg `0.0535` n `6`; index avg `0.1126` n `25`; metal avg `-0.0394` n `20`; unknown avg `-0.6306` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
