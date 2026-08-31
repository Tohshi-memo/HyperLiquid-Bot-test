# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T11:07:30.478804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `-0.1508` n `232`; crypto_major avg `-0.0592` n `8`; equity avg `-0.054` n `128`; fx avg `-0.006` n `6`; index avg `-0.0087` n `26`; metal avg `0.0279` n `20`; unknown avg `0.0672` n `792`
- 1h: commodity avg `-0.0191` n `12`; crypto_alt avg `0.4172` n `232`; crypto_major avg `0.5716` n `8`; equity avg `0.1038` n `128`; fx avg `-0.0231` n `6`; index avg `0.0087` n `26`; metal avg `0.0758` n `20`; unknown avg `-0.5586` n `792`
- 4h: commodity avg `0.3155` n `12`; crypto_alt avg `0.1523` n `232`; crypto_major avg `0.6998` n `8`; equity avg `-0.2642` n `128`; fx avg `-0.0269` n `6`; index avg `-0.037` n `26`; metal avg `0.0843` n `20`; unknown avg `0.321` n `791`
- 24h: commodity avg `0.6268` n `12`; crypto_alt avg `-0.2623` n `231`; crypto_major avg `-0.841` n `8`; equity avg `-0.4462` n `128`; fx avg `-0.1331` n `6`; index avg `-0.0799` n `26`; metal avg `-0.1446` n `20`; unknown avg `-0.1075` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
