# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T15:07:32.803457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `0.2532` n `234`; crypto_major avg `0.3029` n `8`; equity avg `0.3193` n `141`; fx avg `0.0224` n `6`; index avg `0.0556` n `26`; metal avg `0.0717` n `20`; unknown avg `1.8714` n `960`
- 1h: commodity avg `0.2149` n `12`; crypto_alt avg `-1.5222` n `234`; crypto_major avg `-1.0469` n `8`; equity avg `-0.8152` n `141`; fx avg `0.0459` n `6`; index avg `-0.1263` n `26`; metal avg `-0.1531` n `20`; unknown avg `2.4413` n `934`
- 4h: commodity avg `-0.0777` n `12`; crypto_alt avg `-1.0293` n `234`; crypto_major avg `-0.5916` n `8`; equity avg `-0.9458` n `141`; fx avg `0.0352` n `6`; index avg `-0.1247` n `26`; metal avg `-0.1866` n `20`; unknown avg `54.7838` n `904`
- 24h: commodity avg `0.0329` n `12`; crypto_alt avg `-3.5315` n `234`; crypto_major avg `-2.3` n `8`; equity avg `-3.5286` n `141`; fx avg `0.0563` n `6`; index avg `-0.3715` n `26`; metal avg `-1.0883` n `20`; unknown avg `12.171` n `786`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
