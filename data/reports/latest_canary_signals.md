# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T03:22:23.668057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.0955` n `232`; crypto_major avg `0.1535` n `8`; equity avg `0.0777` n `132`; fx avg `0.003` n `6`; index avg `0.0063` n `26`; metal avg `-0.0131` n `20`; unknown avg `2.7217` n `792`
- 1h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.8181` n `232`; crypto_major avg `0.5488` n `8`; equity avg `0.0522` n `132`; fx avg `-0.0076` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.5855` n `790`
- 4h: commodity avg `0.0279` n `12`; crypto_alt avg `0.8715` n `232`; crypto_major avg `0.3678` n `8`; equity avg `-0.0488` n `132`; fx avg `-0.077` n `6`; index avg `-0.0194` n `26`; metal avg `-0.2044` n `20`; unknown avg `0.8412` n `790`
- 24h: commodity avg `0.86` n `12`; crypto_alt avg `-0.3289` n `232`; crypto_major avg `-1.3916` n `8`; equity avg `-2.1908` n `130`; fx avg `-0.0464` n `6`; index avg `-0.3929` n `26`; metal avg `-1.0683` n `20`; unknown avg `-0.0126` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0385`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0317`, n `668`, weak_sample_signal
