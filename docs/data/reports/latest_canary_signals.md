# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T21:07:31.401641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0834` n `13`; crypto_alt avg `-0.1138` n `236`; crypto_major avg `-0.0134` n `8`; equity avg `-0.0288` n `151`; fx avg `0.0046` n `6`; index avg `0.0105` n `26`; metal avg `0.0089` n `20`; unknown avg `3.3382` n `1185`
- 1h: commodity avg `0.0924` n `13`; crypto_alt avg `-0.0206` n `236`; crypto_major avg `0.1783` n `8`; equity avg `0.0686` n `151`; fx avg `0.0043` n `6`; index avg `0.008` n `26`; metal avg `0.0058` n `20`; unknown avg `1.1355` n `1135`
- 4h: commodity avg `0.1472` n `13`; crypto_alt avg `0.1146` n `236`; crypto_major avg `0.315` n `8`; equity avg `-0.5647` n `151`; fx avg `0.0189` n `6`; index avg `-0.1284` n `26`; metal avg `0.0346` n `20`; unknown avg `6.4628` n `1109`
- 24h: commodity avg `0.4494` n `13`; crypto_alt avg `-1.4992` n `236`; crypto_major avg `-1.3329` n `8`; equity avg `-3.374` n `151`; fx avg `0.0441` n `6`; index avg `-0.5956` n `26`; metal avg `-0.1057` n `20`; unknown avg `0.2536` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1622`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
