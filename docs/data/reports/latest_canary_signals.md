# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T02:37:26.162548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.6828` n `234`; crypto_major avg `-0.5214` n `8`; equity avg `-0.1548` n `141`; fx avg `-0.0095` n `6`; index avg `-0.0202` n `26`; metal avg `-0.0744` n `20`; unknown avg `10.022` n `946`
- 1h: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.3771` n `234`; crypto_major avg `-0.0128` n `8`; equity avg `-0.014` n `141`; fx avg `-0.0351` n `6`; index avg `0.0008` n `26`; metal avg `-0.0873` n `20`; unknown avg `2.2462` n `944`
- 4h: commodity avg `-0.2205` n `12`; crypto_alt avg `-0.4151` n `234`; crypto_major avg `0.0799` n `8`; equity avg `0.2688` n `141`; fx avg `-0.0962` n `6`; index avg `0.0642` n `26`; metal avg `-0.0121` n `20`; unknown avg `4.193` n `938`
- 24h: commodity avg `0.4875` n `12`; crypto_alt avg `2.5348` n `234`; crypto_major avg `0.9301` n `8`; equity avg `0.1497` n `141`; fx avg `-0.1029` n `6`; index avg `-0.0165` n `26`; metal avg `-0.1179` n `20`; unknown avg `22.9751` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
