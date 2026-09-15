# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T20:22:35.290769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8983` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.848` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5331` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.2622` n `233`; crypto_major avg `-0.2318` n `8`; equity avg `-0.0396` n `137`; fx avg `0.011` n `6`; index avg `0.0029` n `27`; metal avg `-0.0066` n `20`; unknown avg `2.9342` n `908`
- 1h: commodity avg `0.0535` n `12`; crypto_alt avg `-0.7285` n `233`; crypto_major avg `-0.6667` n `8`; equity avg `-0.054` n `137`; fx avg `0.0156` n `6`; index avg `0.0355` n `27`; metal avg `-0.0357` n `20`; unknown avg `3.608` n `900`
- 4h: commodity avg `0.0861` n `12`; crypto_alt avg `-1.5755` n `233`; crypto_major avg `-1.8095` n `8`; equity avg `-0.2764` n `137`; fx avg `0.0182` n `6`; index avg `0.0385` n `27`; metal avg `0.0888` n `20`; unknown avg `3.4485` n `885`
- 24h: commodity avg `0.5376` n `12`; crypto_alt avg `-5.0324` n `233`; crypto_major avg `-6.064` n `8`; equity avg `-1.1867` n `137`; fx avg `0.2313` n `6`; index avg `-0.0425` n `27`; metal avg `0.1752` n `20`; unknown avg `0.5619` n `843`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
