# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T10:52:30.399168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0725` n `13`; crypto_alt avg `0.0611` n `235`; crypto_major avg `0.1135` n `8`; equity avg `-0.0667` n `150`; fx avg `-0.0098` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.1212` n `1076`
- 1h: commodity avg `0.0725` n `13`; crypto_alt avg `0.0179` n `235`; crypto_major avg `-0.1512` n `8`; equity avg `-0.0983` n `150`; fx avg `-0.0054` n `6`; index avg `-0.0413` n `26`; metal avg `-0.0004` n `20`; unknown avg `2.1621` n `1074`
- 4h: commodity avg `0.1275` n `13`; crypto_alt avg `-1.2247` n `235`; crypto_major avg `-1.0352` n `8`; equity avg `-0.749` n `150`; fx avg `-0.0944` n `6`; index avg `-0.119` n `26`; metal avg `-0.1992` n `20`; unknown avg `0.6949` n `1058`
- 24h: commodity avg `1.3497` n `13`; crypto_alt avg `-4.8547` n `235`; crypto_major avg `-3.3789` n `8`; equity avg `-1.2236` n `150`; fx avg `-0.0963` n `6`; index avg `-0.2696` n `26`; metal avg `-0.4695` n `20`; unknown avg `815.5028` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
