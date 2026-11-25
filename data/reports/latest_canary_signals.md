# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T01:52:26.815094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1156` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.066` n `13`; crypto_alt avg `-0.3895` n `239`; crypto_major avg `-0.611` n `8`; equity avg `-0.6027` n `168`; fx avg `-0.0108` n `6`; index avg `-0.074` n `27`; metal avg `0.0203` n `20`; unknown avg `-0.3015` n `1265`
- 1h: commodity avg `-0.126` n `13`; crypto_alt avg `-0.4837` n `239`; crypto_major avg `-0.8786` n `8`; equity avg `-0.3362` n `168`; fx avg `-0.0316` n `6`; index avg `-0.06` n `27`; metal avg `0.0849` n `20`; unknown avg `-0.3296` n `1255`
- 4h: commodity avg `-0.0973` n `13`; crypto_alt avg `-0.5549` n `239`; crypto_major avg `-1.2312` n `8`; equity avg `-0.8975` n `168`; fx avg `0.0074` n `6`; index avg `-0.1156` n `27`; metal avg `0.0411` n `20`; unknown avg `172.0321` n `1167`
- 24h: commodity avg `0.5996` n `13`; crypto_alt avg `-3.8534` n `239`; crypto_major avg `-3.781` n `8`; equity avg `-5.1011` n `167`; fx avg `0.1344` n `6`; index avg `-0.4958` n `27`; metal avg `-1.1898` n `20`; unknown avg `442.9224` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
