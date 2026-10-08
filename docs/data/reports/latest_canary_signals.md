# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T04:37:29.596353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `13`; crypto_alt avg `0.309` n `235`; crypto_major avg `0.2273` n `8`; equity avg `0.1978` n `150`; fx avg `0.0044` n `6`; index avg `0.0338` n `26`; metal avg `0.0001` n `20`; unknown avg `0.3842` n `1077`
- 1h: commodity avg `0.0281` n `13`; crypto_alt avg `-0.6778` n `235`; crypto_major avg `-0.6417` n `8`; equity avg `-0.0417` n `150`; fx avg `-0.0109` n `6`; index avg `0.0021` n `26`; metal avg `-0.0278` n `20`; unknown avg `0.0386` n `1069`
- 4h: commodity avg `0.2105` n `13`; crypto_alt avg `-0.963` n `235`; crypto_major avg `-0.9434` n `8`; equity avg `-0.4627` n `150`; fx avg `0.0276` n `6`; index avg `-0.0441` n `26`; metal avg `0.3262` n `20`; unknown avg `-0.3864` n `1069`
- 24h: commodity avg `0.4166` n `13`; crypto_alt avg `-0.7387` n `235`; crypto_major avg `-1.9831` n `8`; equity avg `-1.3918` n `150`; fx avg `-0.1274` n `6`; index avg `-0.2382` n `26`; metal avg `-0.205` n `20`; unknown avg `247.1666` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
