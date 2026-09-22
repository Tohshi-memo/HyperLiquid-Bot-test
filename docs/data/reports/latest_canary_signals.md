# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T02:37:27.512921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0392` n `12`; crypto_alt avg `0.5432` n `234`; crypto_major avg `0.3036` n `8`; equity avg `0.0559` n `140`; fx avg `0.0106` n `6`; index avg `-0.0061` n `26`; metal avg `0.0407` n `20`; unknown avg `5.0851` n `944`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `0.2085` n `234`; crypto_major avg `0.0226` n `8`; equity avg `0.0966` n `140`; fx avg `-0.0117` n `6`; index avg `-0.0166` n `26`; metal avg `-0.0166` n `20`; unknown avg `2.1968` n `942`
- 4h: commodity avg `0.1973` n `12`; crypto_alt avg `0.5942` n `234`; crypto_major avg `-0.9713` n `8`; equity avg `0.2349` n `140`; fx avg `-0.1507` n `6`; index avg `-0.002` n `26`; metal avg `-0.0103` n `20`; unknown avg `1.7489` n `936`
- 24h: commodity avg `-0.14` n `12`; crypto_alt avg `4.7312` n `234`; crypto_major avg `4.7504` n `8`; equity avg `2.5231` n `140`; fx avg `-0.2238` n `6`; index avg `0.4951` n `26`; metal avg `-0.0057` n `20`; unknown avg `11.6121` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
