# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T16:52:25.832932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `-0.0486` n `233`; crypto_major avg `0.0167` n `8`; equity avg `0.0766` n `134`; fx avg `-0.0004` n `6`; index avg `0.0006` n `26`; metal avg `0.009` n `20`; unknown avg `-0.0541` n `773`
- 1h: commodity avg `0.0035` n `12`; crypto_alt avg `-0.1579` n `232`; crypto_major avg `0.1684` n `8`; equity avg `-0.0823` n `134`; fx avg `-0.0023` n `6`; index avg `-0.0305` n `26`; metal avg `-0.0234` n `20`; unknown avg `-0.0638` n `765`
- 4h: commodity avg `-0.3519` n `12`; crypto_alt avg `0.6556` n `232`; crypto_major avg `1.0613` n `8`; equity avg `0.9357` n `134`; fx avg `0.0304` n `6`; index avg `-0.0361` n `26`; metal avg `-0.0571` n `20`; unknown avg `-0.2861` n `759`
- 24h: commodity avg `-0.2745` n `12`; crypto_alt avg `0.8903` n `232`; crypto_major avg `0.6186` n `8`; equity avg `1.0826` n `134`; fx avg `-0.0698` n `6`; index avg `-0.0496` n `26`; metal avg `-0.0681` n `20`; unknown avg `7061.2879` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
