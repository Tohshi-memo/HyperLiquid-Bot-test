# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T01:07:27.921939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1179` n `13`; crypto_alt avg `0.074` n `235`; crypto_major avg `0.0426` n `8`; equity avg `0.0559` n `150`; fx avg `-0.0173` n `6`; index avg `0.0026` n `26`; metal avg `0.0016` n `20`; unknown avg `0.0395` n `1132`
- 1h: commodity avg `-0.1476` n `13`; crypto_alt avg `-0.26` n `235`; crypto_major avg `0.1368` n `8`; equity avg `-0.0657` n `150`; fx avg `-0.0276` n `6`; index avg `-0.0315` n `26`; metal avg `0.0668` n `20`; unknown avg `0.0982` n `1124`
- 4h: commodity avg `-0.5428` n `13`; crypto_alt avg `0.3314` n `235`; crypto_major avg `0.3235` n `8`; equity avg `0.1199` n `150`; fx avg `-0.0513` n `6`; index avg `-0.0172` n `26`; metal avg `0.0793` n `20`; unknown avg `-0.0089` n `1096`
- 24h: commodity avg `-0.3738` n `13`; crypto_alt avg `2.3649` n `235`; crypto_major avg `1.1847` n `8`; equity avg `0.3991` n `150`; fx avg `-0.0534` n `6`; index avg `0.0146` n `26`; metal avg `0.1564` n `20`; unknown avg `0.914` n `949`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
