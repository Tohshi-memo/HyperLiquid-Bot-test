# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T01:37:31.109624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0628` n `13`; crypto_alt avg `-0.2493` n `235`; crypto_major avg `-0.1715` n `8`; equity avg `-0.0635` n `150`; fx avg `0.0339` n `6`; index avg `0.0156` n `26`; metal avg `-0.0595` n `20`; unknown avg `0.1489` n `1134`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.459` n `235`; crypto_major avg `-0.092` n `8`; equity avg `-0.3183` n `150`; fx avg `-0.008` n `6`; index avg `-0.0688` n `26`; metal avg `-0.0118` n `20`; unknown avg `-0.1211` n `1124`
- 4h: commodity avg `-0.4794` n `13`; crypto_alt avg `0.1301` n `235`; crypto_major avg `0.3917` n `8`; equity avg `0.0179` n `150`; fx avg `-0.0302` n `6`; index avg `-0.0209` n `26`; metal avg `0.0854` n `20`; unknown avg `0.1994` n `1100`
- 24h: commodity avg `-0.3081` n `13`; crypto_alt avg `1.3381` n `235`; crypto_major avg `0.7269` n `8`; equity avg `0.2622` n `150`; fx avg `-0.0246` n `6`; index avg `0.0047` n `26`; metal avg `0.1411` n `20`; unknown avg `0.6518` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
