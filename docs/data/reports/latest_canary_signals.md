# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T11:07:26.297470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `0.0446` n `235`; crypto_major avg `0.0613` n `8`; equity avg `0.0114` n `150`; fx avg `0.0101` n `6`; index avg `-0.0005` n `26`; metal avg `0.0032` n `20`; unknown avg `-0.0071` n `1115`
- 1h: commodity avg `-0.0029` n `13`; crypto_alt avg `-0.4077` n `235`; crypto_major avg `-0.051` n `8`; equity avg `-0.0109` n `150`; fx avg `0.0057` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0017` n `20`; unknown avg `-0.0509` n `1115`
- 4h: commodity avg `0.0202` n `13`; crypto_alt avg `-0.5544` n `235`; crypto_major avg `-0.1541` n `8`; equity avg `0.01` n `150`; fx avg `0.0161` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.5541` n `1099`
- 24h: commodity avg `0.4319` n `13`; crypto_alt avg `0.8985` n `235`; crypto_major avg `-0.0256` n `8`; equity avg `0.088` n `150`; fx avg `0.0046` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.6154` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
