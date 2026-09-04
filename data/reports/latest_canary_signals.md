# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T16:22:32.233577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.822` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `2.2767` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.2461` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0172` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0678` n `12`; crypto_alt avg `0.1899` n `232`; crypto_major avg `0.0922` n `8`; equity avg `0.135` n `133`; fx avg `-0.0047` n `6`; index avg `0.0368` n `26`; metal avg `0.003` n `20`; unknown avg `0.2687` n `793`
- 1h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.5689` n `232`; crypto_major avg `0.258` n `8`; equity avg `0.3009` n `133`; fx avg `-0.0124` n `6`; index avg `0.0593` n `26`; metal avg `-0.0376` n `20`; unknown avg `0.2544` n `787`
- 4h: commodity avg `0.0676` n `12`; crypto_alt avg `-1.3914` n `232`; crypto_major avg `-2.1785` n `8`; equity avg `0.6435` n `133`; fx avg `-0.0559` n `6`; index avg `0.0982` n `26`; metal avg `-0.1613` n `20`; unknown avg `0.4576` n `725`
- 24h: commodity avg `0.0725` n `12`; crypto_alt avg `-0.8422` n `232`; crypto_major avg `-1.7294` n `8`; equity avg `1.6457` n `133`; fx avg `-0.0894` n `6`; index avg `0.2276` n `26`; metal avg `-0.3022` n `20`; unknown avg `1.0435` n `686`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
