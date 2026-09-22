# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T00:22:27.017809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.2568` n `234`; crypto_major avg `0.3398` n `8`; equity avg `0.0451` n `140`; fx avg `-0.0428` n `6`; index avg `0.0152` n `26`; metal avg `-0.0729` n `20`; unknown avg `0.0428` n `944`
- 1h: commodity avg `0.067` n `12`; crypto_alt avg `0.258` n `234`; crypto_major avg `-0.0706` n `8`; equity avg `0.2314` n `140`; fx avg `-0.0955` n `6`; index avg `0.0382` n `26`; metal avg `0.0326` n `20`; unknown avg `0.4232` n `936`
- 4h: commodity avg `0.1301` n `12`; crypto_alt avg `0.4117` n `234`; crypto_major avg `-0.0172` n `8`; equity avg `0.5882` n `140`; fx avg `-0.1038` n `6`; index avg `0.087` n `26`; metal avg `0.1413` n `20`; unknown avg `0.2234` n `914`
- 24h: commodity avg `-0.5202` n `12`; crypto_alt avg `3.3232` n `234`; crypto_major avg `4.7982` n `8`; equity avg `2.7566` n `140`; fx avg `-0.2099` n `6`; index avg `0.577` n `26`; metal avg `0.1948` n `20`; unknown avg `12.9163` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
