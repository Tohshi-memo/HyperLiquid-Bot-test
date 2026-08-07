# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T12:07:29.967541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `0.1243` n `230`; crypto_major avg `0.2002` n `8`; equity avg `0.0397` n `112`; fx avg `0.0068` n `6`; index avg `0.0177` n `25`; metal avg `-0.02` n `20`; unknown avg `-0.0086` n `782`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.1387` n `230`; crypto_major avg `0.133` n `8`; equity avg `0.0198` n `112`; fx avg `0.0231` n `6`; index avg `0.0235` n `25`; metal avg `-0.1537` n `20`; unknown avg `0.0289` n `782`
- 4h: commodity avg `-0.289` n `12`; crypto_alt avg `0.2033` n `230`; crypto_major avg `0.9558` n `8`; equity avg `0.3116` n `112`; fx avg `-0.0179` n `6`; index avg `0.0387` n `25`; metal avg `-0.0775` n `20`; unknown avg `0.1786` n `782`
- 24h: commodity avg `0.2326` n `12`; crypto_alt avg `0.6756` n `230`; crypto_major avg `0.5747` n `8`; equity avg `2.2376` n `109`; fx avg `-0.0726` n `6`; index avg `0.1472` n `25`; metal avg `0.2065` n `20`; unknown avg `0.3745` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
