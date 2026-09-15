# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T21:37:27.940143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.8765` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8673` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.7823` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.4362` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.1733` n `234`; crypto_major avg `-0.1006` n `8`; equity avg `-0.036` n `137`; fx avg `-0.0021` n `6`; index avg `-0.0037` n `27`; metal avg `-0.0049` n `20`; unknown avg `5.3861` n `919`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.2208` n `234`; crypto_major avg `-0.1296` n `8`; equity avg `-0.0815` n `137`; fx avg `-0.0148` n `6`; index avg `-0.0053` n `27`; metal avg `0.0172` n `20`; unknown avg `15.7162` n `901`
- 4h: commodity avg `-0.0614` n `12`; crypto_alt avg `-2.7155` n `234`; crypto_major avg `-2.8437` n `8`; equity avg `-0.4075` n `137`; fx avg `-0.017` n `6`; index avg `0.0236` n `27`; metal avg `0.0328` n `20`; unknown avg `1.7453` n `876`
- 24h: commodity avg `0.4855` n `12`; crypto_alt avg `-4.2454` n `234`; crypto_major avg `-4.8571` n `8`; equity avg `-1.2835` n `137`; fx avg `0.202` n `6`; index avg `-0.0677` n `27`; metal avg `0.1371` n `20`; unknown avg `2.0786` n `826`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
