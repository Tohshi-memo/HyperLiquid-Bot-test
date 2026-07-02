# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T12:22:28.912951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4091` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2539` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0572` n `12`; crypto_alt avg `0.0498` n `229`; crypto_major avg `0.0018` n `8`; equity avg `0.1062` n `88`; fx avg `-0.01` n `6`; index avg `0.0367` n `25`; metal avg `-0.0705` n `20`; unknown avg `0.2039` n `763`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `0.1159` n `229`; crypto_major avg `0.1447` n `8`; equity avg `0.5474` n `88`; fx avg `-0.0205` n `6`; index avg `0.126` n `25`; metal avg `-0.0523` n `20`; unknown avg `-0.2162` n `763`
- 4h: commodity avg `-0.2257` n `12`; crypto_alt avg `1.2665` n `228`; crypto_major avg `2.1834` n `8`; equity avg `1.0606` n `88`; fx avg `-0.0385` n `6`; index avg `0.1631` n `25`; metal avg `-0.0705` n `20`; unknown avg `-0.0483` n `763`
- 24h: commodity avg `-0.6068` n `12`; crypto_alt avg `3.4332` n `228`; crypto_major avg `4.5766` n `8`; equity avg `-1.2716` n `88`; fx avg `-0.1154` n `6`; index avg `-0.4429` n `25`; metal avg `0.6722` n `20`; unknown avg `1.8004` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
