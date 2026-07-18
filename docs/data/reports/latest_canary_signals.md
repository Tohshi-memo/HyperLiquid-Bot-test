# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T01:37:27.436510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.0443` n `230`; crypto_major avg `-0.0304` n `8`; equity avg `0.0231` n `96`; fx avg `-0.0192` n `6`; index avg `0.0024` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.016` n `769`
- 1h: commodity avg `0.0384` n `12`; crypto_alt avg `-0.1217` n `230`; crypto_major avg `-0.0747` n `8`; equity avg `0.1308` n `96`; fx avg `0.0044` n `6`; index avg `0.0051` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.1675` n `769`
- 4h: commodity avg `-0.022` n `12`; crypto_alt avg `0.0157` n `230`; crypto_major avg `-0.1561` n `8`; equity avg `0.1554` n `96`; fx avg `0.0047` n `6`; index avg `0.0047` n `25`; metal avg `0.085` n `20`; unknown avg `-0.1519` n `769`
- 24h: commodity avg `0.6143` n `12`; crypto_alt avg `-0.5966` n `230`; crypto_major avg `-0.6864` n `8`; equity avg `0.0459` n `94`; fx avg `0.0601` n `6`; index avg `-0.099` n `25`; metal avg `0.0668` n `20`; unknown avg `0.1546` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
