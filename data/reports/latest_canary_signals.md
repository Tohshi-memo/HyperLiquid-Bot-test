# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T22:07:31.800940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `-0.0496` n `238`; crypto_major avg `-0.1196` n `8`; equity avg `-0.0555` n `156`; fx avg `0.0216` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.2475` n `1255`
- 1h: commodity avg `0.005` n `13`; crypto_alt avg `-0.0386` n `238`; crypto_major avg `-0.0438` n `8`; equity avg `0.0044` n `156`; fx avg `-0.0057` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0` n `20`; unknown avg `1.9996` n `1255`
- 4h: commodity avg `0.0337` n `13`; crypto_alt avg `-0.5284` n `238`; crypto_major avg `-0.2912` n `8`; equity avg `-0.0905` n `156`; fx avg `-0.0098` n `6`; index avg `-0.0574` n `27`; metal avg `-0.017` n `20`; unknown avg `182.1106` n `1205`
- 24h: commodity avg `0.0236` n `13`; crypto_alt avg `-0.838` n `238`; crypto_major avg `-0.423` n `8`; equity avg `0.261` n `156`; fx avg `-0.0048` n `6`; index avg `0.032` n `27`; metal avg `0.029` n `20`; unknown avg `3.9691` n `1094`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
