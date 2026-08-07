# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T19:22:28.079795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0657` n `12`; crypto_alt avg `0.0674` n `230`; crypto_major avg `0.2026` n `8`; equity avg `0.0657` n `112`; fx avg `-0.0045` n `6`; index avg `-0.0006` n `25`; metal avg `0.0337` n `20`; unknown avg `0.0028` n `782`
- 1h: commodity avg `-0.2763` n `12`; crypto_alt avg `0.1606` n `230`; crypto_major avg `0.1852` n `8`; equity avg `0.2911` n `112`; fx avg `-0.0065` n `6`; index avg `0.0831` n `25`; metal avg `0.1354` n `20`; unknown avg `-0.1049` n `782`
- 4h: commodity avg `-0.2609` n `12`; crypto_alt avg `0.018` n `230`; crypto_major avg `-0.2833` n `8`; equity avg `0.3292` n `112`; fx avg `-0.0374` n `6`; index avg `0.0421` n `25`; metal avg `0.0378` n `20`; unknown avg `-0.1859` n `782`
- 24h: commodity avg `-0.0662` n `12`; crypto_alt avg `0.006` n `230`; crypto_major avg `0.0386` n `8`; equity avg `1.7509` n `112`; fx avg `-0.1415` n `6`; index avg `0.1055` n `25`; metal avg `0.4631` n `20`; unknown avg `0.0248` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
