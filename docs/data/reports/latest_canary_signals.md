# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T13:22:34.039590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5728` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1305` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0272` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.0283` n `238`; crypto_major avg `0.1863` n `8`; equity avg `-0.1148` n `156`; fx avg `-0.0232` n `6`; index avg `-0.0148` n `27`; metal avg `-0.0199` n `20`; unknown avg `-0.0698` n `1236`
- 1h: commodity avg `-0.3579` n `13`; crypto_alt avg `0.6687` n `238`; crypto_major avg `0.5843` n `8`; equity avg `0.2107` n `156`; fx avg `-0.054` n `6`; index avg `0.0158` n `27`; metal avg `0.0005` n `20`; unknown avg `10.657` n `1230`
- 4h: commodity avg `-0.5311` n `13`; crypto_alt avg `1.2076` n `238`; crypto_major avg `2.0417` n `8`; equity avg `0.0145` n `155`; fx avg `0.0047` n `6`; index avg `-0.0272` n `27`; metal avg `-0.0888` n `20`; unknown avg `10.4686` n `1136`
- 24h: commodity avg `-0.7503` n `13`; crypto_alt avg `-0.3563` n `238`; crypto_major avg `1.1474` n `8`; equity avg `-0.8515` n `155`; fx avg `-0.0172` n `6`; index avg `-0.0729` n `27`; metal avg `-0.5563` n `20`; unknown avg `12.5891` n `980`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
