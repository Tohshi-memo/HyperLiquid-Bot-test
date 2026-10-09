# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T05:37:28.057489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `13`; crypto_alt avg `0.2242` n `235`; crypto_major avg `0.1899` n `8`; equity avg `0.1475` n `150`; fx avg `0.0214` n `6`; index avg `0.0153` n `26`; metal avg `0.1045` n `20`; unknown avg `0.5806` n `1078`
- 1h: commodity avg `-0.0047` n `13`; crypto_alt avg `0.4157` n `235`; crypto_major avg `0.3646` n `8`; equity avg `0.3261` n `150`; fx avg `0.0409` n `6`; index avg `0.0246` n `26`; metal avg `0.1315` n `20`; unknown avg `-0.0401` n `1076`
- 4h: commodity avg `-0.1927` n `13`; crypto_alt avg `1.3842` n `235`; crypto_major avg `1.006` n `8`; equity avg `0.7112` n `150`; fx avg `0.0359` n `6`; index avg `0.1116` n `26`; metal avg `0.2416` n `20`; unknown avg `1.5472` n `1068`
- 24h: commodity avg `0.0182` n `13`; crypto_alt avg `-1.4143` n `235`; crypto_major avg `-2.048` n `8`; equity avg `-1.4095` n `150`; fx avg `0.1308` n `6`; index avg `-0.1507` n `26`; metal avg `0.3355` n `20`; unknown avg `5.754` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
