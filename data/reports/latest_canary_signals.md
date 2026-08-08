# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T06:37:27.062000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `0.0172` n `230`; crypto_major avg `0.0402` n `8`; equity avg `-0.0109` n `112`; fx avg `-0.0005` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.0147` n `784`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.0336` n `8`; equity avg `-0.0643` n `112`; fx avg `0.007` n `6`; index avg `-0.0221` n `25`; metal avg `0.0017` n `20`; unknown avg `0.0077` n `752`
- 4h: commodity avg `0.0162` n `12`; crypto_alt avg `0.3131` n `230`; crypto_major avg `0.4163` n `8`; equity avg `-0.1744` n `112`; fx avg `0.0073` n `6`; index avg `-0.0502` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.1381` n `751`
- 24h: commodity avg `-0.2101` n `12`; crypto_alt avg `-0.1905` n `230`; crypto_major avg `0.5966` n `8`; equity avg `1.1018` n `112`; fx avg `-0.0397` n `6`; index avg `0.1012` n `25`; metal avg `0.0239` n `20`; unknown avg `0.0219` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
