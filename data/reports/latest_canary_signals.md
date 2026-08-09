# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T10:37:29.385860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `-0.0957` n `230`; crypto_major avg `-0.0785` n `8`; equity avg `-0.0009` n `112`; fx avg `-0.0013` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.061` n `785`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.0271` n `230`; crypto_major avg `0.1656` n `8`; equity avg `0.0122` n `112`; fx avg `-0.0022` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.1031` n `785`
- 4h: commodity avg `0.0984` n `12`; crypto_alt avg `-0.2289` n `230`; crypto_major avg `0.0565` n `8`; equity avg `-0.0988` n `112`; fx avg `-0.0076` n `6`; index avg `-0.0037` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.0186` n `785`
- 24h: commodity avg `0.253` n `12`; crypto_alt avg `1.081` n `230`; crypto_major avg `0.3506` n `8`; equity avg `0.4204` n `112`; fx avg `-0.0153` n `6`; index avg `0.0631` n `25`; metal avg `0.0059` n `20`; unknown avg `0.1957` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
