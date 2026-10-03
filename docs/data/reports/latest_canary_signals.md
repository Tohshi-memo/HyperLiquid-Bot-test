# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T12:22:31.494755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `-0.1632` n `235`; crypto_major avg `0.0346` n `8`; equity avg `0.0072` n `143`; fx avg `-0.0025` n `6`; index avg `0.0016` n `26`; metal avg `0.0031` n `20`; unknown avg `0.4976` n `984`
- 1h: commodity avg `0.0107` n `13`; crypto_alt avg `0.0712` n `235`; crypto_major avg `0.2203` n `8`; equity avg `0.0196` n `143`; fx avg `-0.0037` n `6`; index avg `0.0019` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.4063` n `972`
- 4h: commodity avg `-0.0218` n `13`; crypto_alt avg `0.5355` n `235`; crypto_major avg `0.2727` n `8`; equity avg `0.0262` n `143`; fx avg `-0.023` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0131` n `20`; unknown avg `1.6713` n `972`
- 24h: commodity avg `0.6227` n `13`; crypto_alt avg `-2.1764` n `235`; crypto_major avg `-2.2838` n `8`; equity avg `0.3076` n `142`; fx avg `0.0277` n `6`; index avg `0.118` n `26`; metal avg `-0.2084` n `20`; unknown avg `-0.403` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
