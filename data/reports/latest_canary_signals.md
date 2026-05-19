# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T00:22:15.367424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0801` n `12`; crypto_alt avg `0.444` n `228`; crypto_major avg `0.4445` n `8`; equity avg `0.2041` n `66`; fx avg `0.0089` n `6`; index avg `0.0957` n `23`; metal avg `0.0878` n `18`; unknown avg `0.1191` n `383`
- 1h: commodity avg `0.0732` n `12`; crypto_alt avg `0.493` n `228`; crypto_major avg `0.5332` n `8`; equity avg `-0.0166` n `66`; fx avg `0.0908` n `6`; index avg `-0.0288` n `23`; metal avg `-0.0347` n `18`; unknown avg `0.2904` n `383`
- 4h: commodity avg `0.3636` n `12`; crypto_alt avg `1.2184` n `228`; crypto_major avg `0.9571` n `8`; equity avg `0.609` n `66`; fx avg `0.0454` n `6`; index avg `0.2219` n `23`; metal avg `0.6039` n `18`; unknown avg `-0.0367` n `383`
- 24h: commodity avg `0.3636` n `12`; crypto_alt avg `1.7186` n `228`; crypto_major avg `0.589` n `8`; equity avg `0.4104` n `66`; fx avg `0.2295` n `6`; index avg `0.3794` n `23`; metal avg `1.62` n `18`; unknown avg `0.6988` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
