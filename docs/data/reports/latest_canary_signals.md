# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T16:52:31.331676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2741` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.5973` n `228`; crypto_major avg `-0.5492` n `8`; equity avg `-0.4005` n `74`; fx avg `0.0109` n `6`; index avg `-0.2345` n `23`; metal avg `-0.2681` n `18`; unknown avg `-0.0837` n `548`
- 1h: commodity avg `-0.0704` n `12`; crypto_alt avg `-0.8412` n `228`; crypto_major avg `-1.2949` n `8`; equity avg `-0.1456` n `74`; fx avg `0.0309` n `6`; index avg `-0.0208` n `23`; metal avg `-0.0522` n `18`; unknown avg `0.3072` n `548`
- 4h: commodity avg `0.3414` n `12`; crypto_alt avg `-0.0392` n `228`; crypto_major avg `0.0098` n `8`; equity avg `0.0795` n `74`; fx avg `0.0063` n `6`; index avg `-0.367` n `23`; metal avg `0.1699` n `18`; unknown avg `2.2118` n `547`
- 24h: commodity avg `1.4522` n `12`; crypto_alt avg `1.1156` n `228`; crypto_major avg `-0.2788` n `8`; equity avg `2.2401` n `74`; fx avg `-0.0479` n `6`; index avg `1.1067` n `23`; metal avg `-0.7669` n `18`; unknown avg `-0.0039` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.111`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0587`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0569`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0558`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0543`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0467`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0459`, n `669`, weak_sample_signal
