# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T19:07:27.353147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.0038` n `230`; crypto_major avg `-0.0735` n `8`; equity avg `0.0284` n `102`; fx avg `0.0062` n `6`; index avg `-0.0018` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.0015` n `782`
- 1h: commodity avg `0.0161` n `12`; crypto_alt avg `0.1196` n `230`; crypto_major avg `0.2342` n `8`; equity avg `0.1013` n `102`; fx avg `0.0088` n `6`; index avg `0.0051` n `25`; metal avg `0.023` n `20`; unknown avg `0.1646` n `782`
- 4h: commodity avg `-0.1192` n `12`; crypto_alt avg `0.236` n `230`; crypto_major avg `0.6788` n `8`; equity avg `0.4358` n `102`; fx avg `0.0247` n `6`; index avg `0.0407` n `25`; metal avg `0.0876` n `20`; unknown avg `0.2629` n `782`
- 24h: commodity avg `-1.2615` n `12`; crypto_alt avg `1.5229` n `230`; crypto_major avg `1.9642` n `8`; equity avg `1.657` n `102`; fx avg `-0.1209` n `6`; index avg `0.3164` n `25`; metal avg `0.329` n `20`; unknown avg `1.626` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
