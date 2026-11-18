# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T12:52:35.730371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1669` n `13`; crypto_alt avg `-0.079` n `239`; crypto_major avg `0.0169` n `8`; equity avg `-0.0626` n `163`; fx avg `-0.0066` n `6`; index avg `-0.0057` n `27`; metal avg `-0.0494` n `20`; unknown avg `-0.0647` n `1266`
- 1h: commodity avg `-0.0394` n `13`; crypto_alt avg `-0.3022` n `239`; crypto_major avg `-0.1456` n `8`; equity avg `-0.4661` n `163`; fx avg `-0.0071` n `6`; index avg `-0.0529` n `27`; metal avg `-0.1272` n `20`; unknown avg `-0.2732` n `1258`
- 4h: commodity avg `0.2795` n `13`; crypto_alt avg `-0.3568` n `239`; crypto_major avg `-0.7101` n `8`; equity avg `-0.5929` n `163`; fx avg `0.0306` n `6`; index avg `-0.0797` n `27`; metal avg `-0.1368` n `20`; unknown avg `69.2988` n `1246`
- 24h: commodity avg `-0.1502` n `13`; crypto_alt avg `-0.5547` n `239`; crypto_major avg `-0.4441` n `8`; equity avg `-0.5014` n `163`; fx avg `-0.1382` n `6`; index avg `-0.0612` n `27`; metal avg `-1.2487` n `20`; unknown avg `8.6145` n `1097`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
