# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T16:37:28.694511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `-0.0581` n `233`; crypto_major avg `-0.0305` n `8`; equity avg `0.0196` n `136`; fx avg `0.0018` n `6`; index avg `0.0038` n `26`; metal avg `0.0065` n `20`; unknown avg `-0.0566` n `832`
- 1h: commodity avg `0.0278` n `12`; crypto_alt avg `0.0244` n `233`; crypto_major avg `-0.0611` n `8`; equity avg `0.0564` n `136`; fx avg `-0.0035` n `6`; index avg `0.0061` n `26`; metal avg `0.0147` n `20`; unknown avg `-0.2232` n `830`
- 4h: commodity avg `0.0021` n `12`; crypto_alt avg `0.1625` n `233`; crypto_major avg `-0.1369` n `8`; equity avg `0.0209` n `136`; fx avg `0.0034` n `6`; index avg `0.0189` n `26`; metal avg `0.0218` n `20`; unknown avg `1.8542` n `824`
- 24h: commodity avg `-0.1899` n `12`; crypto_alt avg `0.523` n `233`; crypto_major avg `-0.4061` n `8`; equity avg `-0.1259` n `136`; fx avg `-0.0181` n `6`; index avg `0.0337` n `26`; metal avg `-0.015` n `20`; unknown avg `11.5945` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
