# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T09:52:29.149228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.631` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5512` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9419` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `0.2812` n `230`; crypto_major avg `0.4393` n `8`; equity avg `0.0875` n `121`; fx avg `0.0135` n `6`; index avg `0.0022` n `25`; metal avg `-0.0381` n `20`; unknown avg `0.107` n `793`
- 1h: commodity avg `0.0943` n `12`; crypto_alt avg `-0.7512` n `230`; crypto_major avg `-0.5679` n `8`; equity avg `0.0728` n `121`; fx avg `0.0268` n `6`; index avg `-0.0206` n `25`; metal avg `-0.078` n `20`; unknown avg `0.1567` n `793`
- 4h: commodity avg `0.1099` n `12`; crypto_alt avg `2.7041` n `230`; crypto_major avg `2.7409` n `8`; equity avg `0.799` n `121`; fx avg `0.0078` n `6`; index avg `0.0473` n `25`; metal avg `0.1897` n `20`; unknown avg `0.4173` n `777`
- 24h: commodity avg `0.0591` n `12`; crypto_alt avg `7.2871` n `230`; crypto_major avg `7.8646` n `8`; equity avg `0.6402` n `121`; fx avg `-0.0795` n `6`; index avg `0.0184` n `25`; metal avg `0.8533` n `20`; unknown avg `2.5455` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
