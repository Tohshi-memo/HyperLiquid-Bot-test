# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T18:46:01.251961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0372` n `12`; crypto_alt avg `0.0204` n `230`; crypto_major avg `0.0131` n `8`; equity avg `0.0065` n `102`; fx avg `0.0014` n `6`; index avg `0.0045` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0728` n `782`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.1748` n `230`; crypto_major avg `0.3336` n `8`; equity avg `0.0945` n `102`; fx avg `0.015` n `6`; index avg `0.0047` n `25`; metal avg `0.0333` n `20`; unknown avg `0.1347` n `782`
- 4h: commodity avg `-0.1383` n `12`; crypto_alt avg `0.2468` n `230`; crypto_major avg `0.7945` n `8`; equity avg `0.4134` n `102`; fx avg `0.0202` n `6`; index avg `0.0438` n `25`; metal avg `0.0854` n `20`; unknown avg `1.5927` n `782`
- 24h: commodity avg `-1.2901` n `12`; crypto_alt avg `1.9614` n `230`; crypto_major avg `2.482` n `8`; equity avg `1.6088` n `102`; fx avg `-0.1228` n `6`; index avg `0.3174` n `25`; metal avg `0.3601` n `20`; unknown avg `1.6888` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
