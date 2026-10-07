# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T14:52:40.789036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1079` n `13`; crypto_alt avg `-0.1226` n `235`; crypto_major avg `-0.0918` n `8`; equity avg `-0.0372` n `150`; fx avg `0.0015` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0086` n `20`; unknown avg `-0.3157` n `1076`
- 1h: commodity avg `0.0662` n `13`; crypto_alt avg `-0.5483` n `235`; crypto_major avg `-0.4783` n `8`; equity avg `0.129` n `150`; fx avg `0.001` n `6`; index avg `0.0383` n `26`; metal avg `0.1144` n `20`; unknown avg `-0.2992` n `1062`
- 4h: commodity avg `0.1444` n `13`; crypto_alt avg `-1.2857` n `235`; crypto_major avg `-0.9432` n `8`; equity avg `-0.4203` n `150`; fx avg `-0.0269` n `6`; index avg `-0.1263` n `26`; metal avg `-0.1608` n `20`; unknown avg `0.306` n `1022`
- 24h: commodity avg `1.3419` n `13`; crypto_alt avg `-6.2691` n `235`; crypto_major avg `-4.5195` n `8`; equity avg `-2.0475` n `150`; fx avg `-0.1533` n `6`; index avg `-0.4374` n `26`; metal avg `-0.5116` n `20`; unknown avg `17.3096` n `984`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
