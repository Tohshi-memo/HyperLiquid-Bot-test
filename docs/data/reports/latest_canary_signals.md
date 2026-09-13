# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T03:52:27.459603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.111` n `233`; crypto_major avg `-0.0852` n `8`; equity avg `0.0039` n `136`; fx avg `-0.0153` n `6`; index avg `0.0078` n `26`; metal avg `0.0007` n `20`; unknown avg `2.8196` n `838`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `-0.0914` n `233`; crypto_major avg `-0.3301` n `8`; equity avg `-0.0468` n `136`; fx avg `0.0004` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0024` n `20`; unknown avg `1.4292` n `836`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `0.2656` n `233`; crypto_major avg `-0.2685` n `8`; equity avg `-0.1534` n `136`; fx avg `0.0062` n `6`; index avg `-0.0333` n `26`; metal avg `0.0073` n `20`; unknown avg `4.037` n `806`
- 24h: commodity avg `0.0014` n `12`; crypto_alt avg `0.9159` n `233`; crypto_major avg `-0.0164` n `8`; equity avg `-0.4781` n `136`; fx avg `-0.0115` n `6`; index avg `-0.0571` n `26`; metal avg `0.0385` n `20`; unknown avg `0.6343` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
