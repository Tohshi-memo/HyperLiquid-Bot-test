# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T18:07:32.941729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0837` n `12`; crypto_alt avg `-0.0917` n `232`; crypto_major avg `-0.0523` n `8`; equity avg `0.1665` n `133`; fx avg `0.0008` n `6`; index avg `0.0007` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.1729` n `790`
- 1h: commodity avg `0.0446` n `12`; crypto_alt avg `0.2124` n `232`; crypto_major avg `0.4167` n `8`; equity avg `0.3469` n `133`; fx avg `-0.0053` n `6`; index avg `0.0243` n `26`; metal avg `0.0501` n `20`; unknown avg `16.2683` n `790`
- 4h: commodity avg `0.3768` n `12`; crypto_alt avg `-0.2457` n `232`; crypto_major avg `-0.2133` n `8`; equity avg `0.3666` n `133`; fx avg `-0.0123` n `6`; index avg `0.0733` n `26`; metal avg `-0.1098` n `20`; unknown avg `-0.3455` n `789`
- 24h: commodity avg `0.3478` n `12`; crypto_alt avg `-0.2823` n `232`; crypto_major avg `-0.5272` n `8`; equity avg `0.3483` n `133`; fx avg `-0.368` n `6`; index avg `0.105` n `26`; metal avg `0.3183` n `20`; unknown avg `-0.3386` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0377`, n `668`, weak_sample_signal
