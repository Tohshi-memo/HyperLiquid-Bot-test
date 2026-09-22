# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T12:52:49.707993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `0.3307` n `234`; crypto_major avg `0.0376` n `8`; equity avg `-0.0316` n `140`; fx avg `0.0027` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0017` n `20`; unknown avg `1.8498` n `944`
- 1h: commodity avg `0.1113` n `12`; crypto_alt avg `0.7184` n `234`; crypto_major avg `0.3159` n `8`; equity avg `-0.0135` n `140`; fx avg `0.0389` n `6`; index avg `-0.0109` n `26`; metal avg `0.1735` n `20`; unknown avg `-0.0469` n `936`
- 4h: commodity avg `0.016` n `12`; crypto_alt avg `-0.3343` n `234`; crypto_major avg `-0.1839` n `8`; equity avg `0.1739` n `140`; fx avg `0.0665` n `6`; index avg `0.0321` n `26`; metal avg `0.0947` n `20`; unknown avg `2.6159` n `934`
- 24h: commodity avg `-0.421` n `12`; crypto_alt avg `0.5087` n `234`; crypto_major avg `1.5209` n `8`; equity avg `0.7377` n `140`; fx avg `-0.2442` n `6`; index avg `0.2236` n `26`; metal avg `-0.1802` n `20`; unknown avg `1108.4247` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
