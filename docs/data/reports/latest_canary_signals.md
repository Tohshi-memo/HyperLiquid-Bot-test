# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T21:42:35.784346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0419` n `12`; crypto_alt avg `-0.0252` n `230`; crypto_major avg `-0.0028` n `8`; equity avg `0.0314` n `112`; fx avg `-0.0017` n `6`; index avg `-0.0131` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.0421` n `784`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.0244` n `230`; crypto_major avg `0.0201` n `8`; equity avg `0.0284` n `112`; fx avg `0.0012` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0089` n `20`; unknown avg `-0.0971` n `784`
- 4h: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.0373` n `230`; crypto_major avg `-0.1877` n `8`; equity avg `0.1177` n `112`; fx avg `0.0003` n `6`; index avg `0.0068` n `25`; metal avg `0.0022` n `20`; unknown avg `0.3122` n `784`
- 24h: commodity avg `0.1039` n `12`; crypto_alt avg `1.7584` n `230`; crypto_major avg `1.3973` n `8`; equity avg `0.695` n `112`; fx avg `0.0004` n `6`; index avg `0.0288` n `25`; metal avg `0.045` n `20`; unknown avg `0.1959` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
