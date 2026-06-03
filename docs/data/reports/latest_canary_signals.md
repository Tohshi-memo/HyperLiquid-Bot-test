# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T02:07:24.425945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0235` n `12`; crypto_alt avg `0.2478` n `228`; crypto_major avg `0.0905` n `8`; equity avg `0.1364` n `69`; fx avg `-0.0009` n `6`; index avg `0.1247` n `23`; metal avg `-0.0047` n `18`; unknown avg `1.01` n `422`
- 1h: commodity avg `-0.0633` n `12`; crypto_alt avg `0.0233` n `228`; crypto_major avg `-0.3333` n `8`; equity avg `-0.0001` n `69`; fx avg `-0.025` n `6`; index avg `-0.1018` n `23`; metal avg `0.0968` n `18`; unknown avg `0.7123` n `422`
- 4h: commodity avg `0.2914` n `12`; crypto_alt avg `-0.1918` n `228`; crypto_major avg `-0.5611` n `8`; equity avg `-0.4045` n `69`; fx avg `0.0044` n `6`; index avg `0.2939` n `23`; metal avg `-0.4005` n `18`; unknown avg `-0.4479` n `422`
- 24h: commodity avg `0.7169` n `12`; crypto_alt avg `-2.6574` n `228`; crypto_major avg `-4.7337` n `8`; equity avg `1.9806` n `69`; fx avg `0.0362` n `6`; index avg `1.6803` n `23`; metal avg `0.1679` n `18`; unknown avg `-0.8768` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
