# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T20:01:53.597698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `0.0468` n `229`; crypto_major avg `-0.0895` n `8`; equity avg `-0.0904` n `88`; fx avg `-0.0027` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.1086` n `765`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `0.2435` n `229`; crypto_major avg `0.1876` n `8`; equity avg `-0.0887` n `88`; fx avg `-0.0078` n `6`; index avg `-0.0107` n `25`; metal avg `-0.0126` n `20`; unknown avg `0.0866` n `765`
- 4h: commodity avg `-0.0159` n `12`; crypto_alt avg `0.453` n `229`; crypto_major avg `0.6975` n `8`; equity avg `-0.0453` n `88`; fx avg `-0.0095` n `6`; index avg `0.0445` n `25`; metal avg `0.0484` n `20`; unknown avg `1.0291` n `765`
- 24h: commodity avg `0.1405` n `12`; crypto_alt avg `2.8224` n `229`; crypto_major avg `2.7557` n `8`; equity avg `1.6969` n `88`; fx avg `-0.0645` n `6`; index avg `0.5121` n `25`; metal avg `0.5722` n `20`; unknown avg `8.4948` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
