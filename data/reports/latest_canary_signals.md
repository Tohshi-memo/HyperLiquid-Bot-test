# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T11:22:24.027354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `12`; crypto_alt avg `0.3109` n `233`; crypto_major avg `0.2367` n `8`; equity avg `0.0127` n `134`; fx avg `0.0013` n `6`; index avg `0.0008` n `26`; metal avg `-0.0425` n `20`; unknown avg `1.4657` n `797`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `0.1494` n `233`; crypto_major avg `0.015` n `8`; equity avg `-0.1756` n `134`; fx avg `0.0216` n `6`; index avg `-0.0573` n `26`; metal avg `-0.3648` n `20`; unknown avg `1.007` n `795`
- 4h: commodity avg `0.1892` n `12`; crypto_alt avg `-0.2453` n `233`; crypto_major avg `-0.1395` n `8`; equity avg `-0.5215` n `134`; fx avg `0.0516` n `6`; index avg `-0.1207` n `26`; metal avg `-0.6079` n `20`; unknown avg `0.5718` n `789`
- 24h: commodity avg `-0.0805` n `12`; crypto_alt avg `-3.7209` n `233`; crypto_major avg `-2.477` n `8`; equity avg `-0.9429` n `134`; fx avg `0.107` n `6`; index avg `-0.0533` n `26`; metal avg `-0.4013` n `20`; unknown avg `-0.2362` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
