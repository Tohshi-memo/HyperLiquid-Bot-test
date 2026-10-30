# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T06:52:28.816476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1556` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1282` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.5887` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0584` n `13`; crypto_alt avg `0.0058` n `238`; crypto_major avg `-0.0517` n `8`; equity avg `-0.1392` n `156`; fx avg `-0.0105` n `6`; index avg `-0.0077` n `27`; metal avg `-0.0215` n `20`; unknown avg `2.6551` n `1260`
- 1h: commodity avg `-0.0811` n `13`; crypto_alt avg `0.2764` n `238`; crypto_major avg `0.2018` n `8`; equity avg `0.0814` n `156`; fx avg `-0.0178` n `6`; index avg `0.0414` n `27`; metal avg `-0.1329` n `20`; unknown avg `3.3197` n `1236`
- 4h: commodity avg `-0.0892` n `13`; crypto_alt avg `2.5766` n `238`; crypto_major avg `2.039` n `8`; equity avg `0.4503` n `156`; fx avg `-0.0807` n `6`; index avg `0.0981` n `27`; metal avg `-0.1166` n `20`; unknown avg `5.242` n `1216`
- 24h: commodity avg `-0.1182` n `13`; crypto_alt avg `-2.9264` n `238`; crypto_major avg `0.3739` n `8`; equity avg `-2.7457` n `155`; fx avg `0.1103` n `6`; index avg `-0.3553` n `27`; metal avg `-0.6932` n `20`; unknown avg `29.7549` n `980`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
