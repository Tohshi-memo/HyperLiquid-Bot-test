# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T11:52:26.737447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.029` n `230`; crypto_major avg `-0.0489` n `8`; equity avg `0.0066` n `112`; fx avg `-0.0003` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0035` n `20`; unknown avg `-0.019` n `785`
- 1h: commodity avg `-0.1216` n `12`; crypto_alt avg `0.0832` n `230`; crypto_major avg `-0.0473` n `8`; equity avg `0.0272` n `112`; fx avg `-0.0076` n `6`; index avg `0.0024` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.048` n `785`
- 4h: commodity avg `-0.0349` n `12`; crypto_alt avg `0.1517` n `230`; crypto_major avg `0.0189` n `8`; equity avg `-0.0301` n `112`; fx avg `-0.0034` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0143` n `20`; unknown avg `-0.0412` n `785`
- 24h: commodity avg `0.1633` n `12`; crypto_alt avg `1.1938` n `230`; crypto_major avg `0.2392` n `8`; equity avg `0.4199` n `112`; fx avg `-0.0166` n `6`; index avg `0.0276` n `25`; metal avg `0.0173` n `20`; unknown avg `0.244` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
