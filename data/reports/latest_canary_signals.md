# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T02:22:29.239667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0824` n `12`; crypto_alt avg `0.9194` n `234`; crypto_major avg `0.5528` n `8`; equity avg `0.0516` n `141`; fx avg `0.0099` n `6`; index avg `0.0054` n `26`; metal avg `0.0878` n `20`; unknown avg `2.3198` n `945`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `0.6218` n `234`; crypto_major avg `-0.1345` n `8`; equity avg `-0.0311` n `141`; fx avg `0.0139` n `6`; index avg `-0.0233` n `26`; metal avg `-0.0442` n `20`; unknown avg `1.2848` n `943`
- 4h: commodity avg `-0.1272` n `12`; crypto_alt avg `0.2943` n `234`; crypto_major avg `-0.3674` n `8`; equity avg `-0.3391` n `141`; fx avg `0.0202` n `6`; index avg `-0.0797` n `26`; metal avg `-0.0884` n `20`; unknown avg `1.3254` n `937`
- 24h: commodity avg `0.4314` n `12`; crypto_alt avg `-4.0296` n `234`; crypto_major avg `-3.9096` n `8`; equity avg `-1.5301` n `140`; fx avg `0.0841` n `6`; index avg `-0.3089` n `26`; metal avg `-0.65` n `20`; unknown avg `583.5656` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
