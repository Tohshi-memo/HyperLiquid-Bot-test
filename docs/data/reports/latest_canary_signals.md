# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T05:37:30.307782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.063` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7753` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6487` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `-0.568` n `234`; crypto_major avg `-0.5885` n `8`; equity avg `-0.0562` n `141`; fx avg `-0.0082` n `6`; index avg `0.0016` n `26`; metal avg `-0.0225` n `20`; unknown avg `0.9013` n `962`
- 1h: commodity avg `0.0834` n `12`; crypto_alt avg `-1.1605` n `234`; crypto_major avg `-1.0068` n `8`; equity avg `-0.2566` n `141`; fx avg `0.0282` n `6`; index avg `-0.0256` n `26`; metal avg `-0.1202` n `20`; unknown avg `25.8154` n `960`
- 4h: commodity avg `0.192` n `12`; crypto_alt avg `-2.7923` n `234`; crypto_major avg `-1.871` n `8`; equity avg `-0.8496` n `141`; fx avg `-0.0124` n `6`; index avg `-0.0957` n `26`; metal avg `-0.2223` n `20`; unknown avg `289.2883` n `940`
- 24h: commodity avg `-0.2948` n `12`; crypto_alt avg `-2.6302` n `234`; crypto_major avg `-2.4899` n `8`; equity avg `-1.6496` n `141`; fx avg `0.0685` n `6`; index avg `-0.1568` n `26`; metal avg `-0.8054` n `20`; unknown avg `6.1011` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
