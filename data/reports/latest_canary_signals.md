# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T01:37:34.508220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `13`; crypto_alt avg `-0.345` n `236`; crypto_major avg `-0.1109` n `8`; equity avg `-0.0436` n `151`; fx avg `0.0034` n `6`; index avg `-0.0256` n `26`; metal avg `-0.0308` n `20`; unknown avg `4.2613` n `1136`
- 1h: commodity avg `0.0008` n `13`; crypto_alt avg `-0.3726` n `236`; crypto_major avg `-0.3471` n `8`; equity avg `0.3547` n `151`; fx avg `0.0217` n `6`; index avg `0.0343` n `26`; metal avg `0.0218` n `20`; unknown avg `0.2439` n `1134`
- 4h: commodity avg `-0.0155` n `13`; crypto_alt avg `-0.4208` n `236`; crypto_major avg `-0.5466` n `8`; equity avg `-0.0732` n `151`; fx avg `0.0762` n `6`; index avg `-0.049` n `26`; metal avg `-0.1111` n `20`; unknown avg `-0.1576` n `1096`
- 24h: commodity avg `-0.0636` n `13`; crypto_alt avg `0.6849` n `236`; crypto_major avg `0.2996` n `8`; equity avg `1.4815` n `151`; fx avg `0.0082` n `6`; index avg `0.2369` n `26`; metal avg `0.1398` n `20`; unknown avg `25.3683` n `910`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0932`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0891`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0889`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.065`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
