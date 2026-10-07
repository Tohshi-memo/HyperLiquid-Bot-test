# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T04:07:25.419590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1864` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9659` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8387` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5319` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `-0.5258` n `235`; crypto_major avg `-0.2355` n `8`; equity avg `-0.0389` n `150`; fx avg `0.002` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0146` n `20`; unknown avg `-0.3089` n `1068`
- 1h: commodity avg `0.0668` n `13`; crypto_alt avg `-0.5434` n `235`; crypto_major avg `-0.1941` n `8`; equity avg `0.0852` n `150`; fx avg `-0.0068` n `6`; index avg `-0.0005` n `26`; metal avg `0.0163` n `20`; unknown avg `0.0885` n `1068`
- 4h: commodity avg `0.1781` n `13`; crypto_alt avg `-3.2215` n `235`; crypto_major avg `-2.0083` n `8`; equity avg `-0.4764` n `150`; fx avg `-0.0343` n `6`; index avg `-0.0424` n `26`; metal avg `-0.1696` n `20`; unknown avg `1.6041` n `1068`
- 24h: commodity avg `0.5311` n `13`; crypto_alt avg `-3.251` n `235`; crypto_major avg `-2.5156` n `8`; equity avg `0.0041` n `149`; fx avg `0.0493` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0542` n `20`; unknown avg `871.066` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
