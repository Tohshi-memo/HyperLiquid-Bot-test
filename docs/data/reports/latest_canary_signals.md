# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T17:52:35.587712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `0.3391` n `235`; crypto_major avg `0.242` n `8`; equity avg `0.037` n `151`; fx avg `-0.0029` n `6`; index avg `0.0062` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.1714` n `1134`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `0.0788` n `235`; crypto_major avg `-0.1866` n `8`; equity avg `-0.0114` n `151`; fx avg `0.0028` n `6`; index avg `-0.0065` n `26`; metal avg `0.0395` n `20`; unknown avg `0.0714` n `1132`
- 4h: commodity avg `0.1362` n `13`; crypto_alt avg `-1.4887` n `235`; crypto_major avg `-1.0085` n `8`; equity avg `-0.9376` n `151`; fx avg `-0.0497` n `6`; index avg `-0.0665` n `26`; metal avg `-0.0682` n `20`; unknown avg `0.2311` n `1074`
- 24h: commodity avg `0.5008` n `13`; crypto_alt avg `-3.184` n `235`; crypto_major avg `-2.3832` n `8`; equity avg `-3.4914` n `151`; fx avg `-0.165` n `6`; index avg `-0.3392` n `26`; metal avg `-0.1796` n `20`; unknown avg `-0.0221` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2099`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1911`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.136`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.127`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1111`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0959`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
