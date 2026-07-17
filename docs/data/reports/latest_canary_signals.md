# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T02:52:28.199132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.0473` n `230`; crypto_major avg `-0.0765` n `8`; equity avg `-0.0736` n `94`; fx avg `0.0075` n `6`; index avg `-0.0112` n `25`; metal avg `-0.026` n `20`; unknown avg `0.9294` n `768`
- 1h: commodity avg `-0.1132` n `12`; crypto_alt avg `-0.2849` n `230`; crypto_major avg `-0.089` n `8`; equity avg `-0.5657` n `94`; fx avg `0.0137` n `6`; index avg `-0.0405` n `25`; metal avg `-0.098` n `20`; unknown avg `0.7758` n `768`
- 4h: commodity avg `-0.0957` n `12`; crypto_alt avg `-0.8852` n `230`; crypto_major avg `-0.9263` n `8`; equity avg `-1.812` n `94`; fx avg `-0.001` n `6`; index avg `-0.2497` n `25`; metal avg `-0.1765` n `20`; unknown avg `0.0332` n `768`
- 24h: commodity avg `-0.1758` n `12`; crypto_alt avg `-2.4741` n `230`; crypto_major avg `-3.1562` n `8`; equity avg `-5.5515` n `94`; fx avg `-0.1414` n `6`; index avg `-0.6984` n `25`; metal avg `-0.8109` n `20`; unknown avg `-0.6886` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
